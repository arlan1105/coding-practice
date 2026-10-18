def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    unit = ['B', 'KB', 'MB', 'GB', 'TB']
    
    if video_unit not in unit[:4]: 
        return "Invalid video unit"
    if drive_unit not in unit[3:]: 
        return "Invalid drive unit"

    conv = 1000**((unit.index(drive_unit)) - (unit.index(video_unit)))

    return conv * drive_size // video_size

print(number_of_videos(500000, "KB", 2, "TB"))
print(number_of_videos(1.5, "GB", 2.2, "TB"))

# return conv * round(drive_size * 10**6) // round(video_size * 10**6)