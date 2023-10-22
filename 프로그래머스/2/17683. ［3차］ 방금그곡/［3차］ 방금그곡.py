def solution(m, musicinfos):
    music_list = []
    for musicinfo in musicinfos:
        start_time, end_time, name, scale = musicinfo.split(',')
        
        start_hour, start_min = list(map(int, start_time.split(':')))
        start_timestamp = 60 * start_hour + start_min
        end_hour, end_min = list(map(int, end_time.split(':')))
        end_timestamp = 60 * end_hour + end_min
        playtime = end_timestamp - start_timestamp
        
        scale_list = str_to_scale_list(scale)
    
        # 총 재생된 scale의 내용을 구합니다.
        total_scale_list = []
        repeat_cnt, leftover_cnt = divmod(playtime, len(scale_list))
        total_scale_list += scale_list * repeat_cnt
        total_scale_list += scale_list[:leftover_cnt]
        
        music_list.append([name, playtime, total_scale_list])
    
    m_scale_list = str_to_scale_list(m)
    m_len = len(m_scale_list)
    
    possible_music_list = []
    for music in music_list:
        name = music[0]
        music_scale_list = music[2]
        for i in range(len(music_scale_list) - len(m_scale_list) + 1):
            isValid = True
            for j in range(len(m_scale_list)):
                if music_scale_list[i+j] != m_scale_list[j]:
                    isValid = False
                    break
            if isValid == True:
                possible_music_list.append(music)
    if len(possible_music_list) == 0:
        return "(None)"
    
    possible_music_list.sort(key=lambda x:-x[1])
    
    return possible_music_list[0][0]
    
def str_to_scale_list(scale_str):
    scale_list = []
    i = 0
    while i < len(scale_str):
        if i < (len(scale_str) - 1) and scale_str[i+1] == '#':
            scale_list.append(scale_str[i:i+2])
            i += 2
        else:
            scale_list.append(scale_str[i])
            i += 1
    return scale_list