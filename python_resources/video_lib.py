from video_lib import video_manager


def update_containers(containers_path):
    from utils import FileHandlers
    video_data = {}
    for container_id in video_manager(containers_path).ids:
        container_data = video_manager(containers_path).get_container_data(container_id)
        video_data.update(container_data['video_data'])
        FileHandlers.save_file(
            path="../video_app/video_data.json",
            data=video_data
        )
        FileHandlers.save_file(
            path=f"{ video_manager(containers_path).__dict__[container_id]['path']}/info_container.json",
            data=container_data['info_container']
        )
