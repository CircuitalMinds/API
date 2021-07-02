function config_player ( app ) {
    app.vol.adjusts = vol_adjusts(10);
    app.vol.set_level = function ( adjust_to ) {
        index = this.vol.adjusts.indexOf(this.player.volume);
        if ( adjust_to == '+' & this.player.volume != 1 ) {
            this.player.volume = this.vol.adjusts[index + 1]
        } else if ( adjust_to == '-' & this.player.volume != 0 ) {
            this.player.volume = this.vol.adjusts[index - 1]
        }
    };
    app.GetData('minus').onclick = app.vol.set_level('-');
    app.GetData('plus').onclick = app.vol.set_level('+');

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
        this.GetData('video-media').innerHTML = titles[index];
        this.player.setAttribute('src', videos[titles[index]]);
    };
    app.on_play = function () {
        if ( this.player.src == '' ) {
            video = this.get_random_video(this.get_random_list());
            this.GetData('video-title').innerHTML = video.title;
            this.player.setAttribute('src', video.url);
            this.player.play();
        } else {
            this.player.play();
        }
    };
    app.on_pause = function () {
        this.player.pause();
    };
    app.GetData('previous').onclick = app.set_video('previous');
    app.GetData('next').onclick = app.set_video('next');
    app.GetData('play').onclick = app.set_video('play');
    app.GetData('pause').onclick = app.set_video('pause');
};

function vol_adjusts ( step_size ) {
	vol = [];
	steps = Math.round(1.0 / step_size);
	for ( var i = 0; i <= steps; i++ ) {
		vol.push(step_size * i);
	};
	return vol
};