def solution(book_time_list):
    book_list = []
    for book_time in book_time_list:
        start_time_str, end_time_str = book_time
        start_time = int(start_time_str.split(':')[0]) * 60 + int(start_time_str.split(':')[1])
        end_time = int(end_time_str.split(':')[0]) * 60 + int(end_time_str.split(':')[1])
        book_list.append([start_time, end_time])

    # 최대한 많은 예약을 받을 수 있도록 정렬
    book_list.sort(key=lambda x:[x[0], x[1]])
    
    count = 0
    while book_list:
        count += 1
        completed_book_idx_list = book_most_room(book_list)
        book_list = [book_list[i] for i in range(len(book_list)) if i not in completed_book_idx_list]
    
    return count

def book_most_room(book_list):
    completed_book_idx_list = []
    current_end_time = -10
    for i, book in enumerate(book_list):
        if book[0] >= current_end_time + 10:
            completed_book_idx_list.append(i)
            current_end_time = book[1]
    return completed_book_idx_list