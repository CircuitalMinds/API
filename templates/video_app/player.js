function config_player ( app ) {
    app.vol.adjusts = vol_adjusts(0.1);
    app.vol.set_level = function ( adjust_to ) {
        index = this.adjusts.indexOf(app.player.volume);
        if ( adjust_to == '+' & app.player.volume != 1 ) {
            app.player.volume = this.adjusts[index + 1]
        } else if ( adjust_to == '-' & app.player.volume != 0 ) {
            app.player.volume = this.adjusts[index - 1]
        }
    };
    app.GetData('minus').onclick = function () {app.vol.set_level('-')};
    app.GetData('plus').onclick = function () {app.vol.set_level('+')};

    app.set_video = function ( change_to  ) {
        video = this.get_current_video();
        videos = this.videos[video.container_id];
        titles = this.get_titles(videos);
        index = video.index;
        if ( change_to == 'previous' & index > 0 ) {
            index = index - 1;
        } else if ( change_to == 'next' & index < titles.length - 1 ) {
            index = index + 1;
        };
        this.GetData('video-title').innerHTML = titles[index];
        this.GetData('video-media').setAttribute('src', videos[titles[index]].url);
        this.GetData('video-media').play();
    };
    app.set_video_from_list = function ( index ) {
	title = $("li #title")[index].textContent;
    	video = this.videos[title[0].toLowerCase()][title];
        this.GetData('video-title').innerHTML = title;
        this.GetData('video-media').setAttribute('src', video.url);
        this.GetData('video-media').play();
    };

    app.GetData('previous').onclick = function () { app.set_video('previous') };
    app.GetData('next').onclick = function () { app.set_video('next') };
    app.GetData('play').onclick = function () {
        if ( app.GetData('video-media').src == '' ) {
            video = app.get_random_video(app.get_random_list());
            app.GetData('video-title').innerHTML = video.title;
            app.GetData('video-media').setAttribute('src', video.url);
            app.GetData('video-media').play();
        } else {
            app.GetData('video-media').play();
        }
    };
    app.GetData('pause').onclick = function () {app.GetData('video-media').pause()};
    app.on_play = app.GetData('play').onclick;
    app.on_pause = app.GetData('pause').onclick;
};

function vol_adjusts ( step_size ) {
	vol = [];
	steps = Math.round(1.0 / step_size);
	for ( var i = 0; i <= steps; i++ ) {
		vol.push(step_size * i);
	};
	return vol
};
