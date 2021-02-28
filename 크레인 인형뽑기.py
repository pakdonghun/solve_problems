def solution(board, moves):
    basket=[]
    count=0
    for crane in moves:
        for i in board:
            if not i[crane-1] ==0:
                basket.append(i[crane-1])
                i[crane-1]=0  
                break
        if len(basket)>1:
            if basket[-1]==basket[-2]:
                count+=2
                del basket[-1]
                del basket[-1]
            
    return count
