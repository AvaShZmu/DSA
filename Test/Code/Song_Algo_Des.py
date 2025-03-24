def create_playlist(songs, target_duration):
    dp = [0] * (target_duration + 1)
    tracker = {i: [] for i in range(target_duration + 1)}

    for title, duration in songs:
        for i in range(target_duration, duration - 1, -1):
            if dp[i - duration] + duration > dp[i]:
                dp[i] = dp[i - duration] + duration
                tracker[i] = tracker[i - duration] + [title]

    best_duration = max(dp)
    return tracker[best_duration], best_duration


if __name__ == '__main__':
    songs = [
        ("Song A", 180),
        ("Song B", 240),
        ("Song C", 120),
        ("Song D", 260)
    ]

    target_duration = 600
    playlist, total_duration = create_playlist(songs, target_duration)

    print("Playlist:", playlist)
    print("Total Duration:", total_duration)