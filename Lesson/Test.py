import time
import asyncio

# async def download_photo(photo_count, limit):
#     while photo_count < limit:
#         await asyncio.sleep(1)
#         photo_count += 1
#         print(f'Photo {photo_count}...')
#
# async def download_video(video_count, limit):
#     while video_count < limit:
#         await asyncio.sleep(5)
#         video_count += 1
#         print(f'Video {video_count}...')
#
# async def download_music(music_count, limit):
#     while music_count < limit:
#         await asyncio.sleep(3)
#         music_count += 1
#         print(f'Music {music_count}...')
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     music_count = 0
#     task_list = [
#         download_photo(photo_count, 15),
#         download_video(video_count, 5),
#         download_music(music_count, 10)
#     ]
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())


async def download_photo(photo_count):
    await asyncio.sleep(1)
    print(f'Photo {photo_count}...')

async def main():
    limit = int(input('Enter amount: '))
    current_photo = 0
    task_list = []
    while current_photo < limit:
        current_photo += 1
        task = asyncio.create_task(download_photo(current_photo))
        task_list.append(task)

        await asyncio.gather(*task_list)

asyncio.run(main())