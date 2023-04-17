import time
import datetime


#print(time.localtime())
#print(time.strftime("%Y-%m-%d %H:%M:%S"))

today = datetime.date.today()
td = datetime.timedelta(days=20)
print(today)
print(today + td)


""" 
[ start_________________________________________________
repository
    commit들을 모아 놓은 것이다.
    repository는 HEAD도 정의하는데, head는, 현재 working tree가유래한
    branch나 commit을나타낸다. respoitory는 특정 commit 들에 이름을 붙이고,
    이 커밋들을 branch혹은 tag이라고 부른다.
the Index (staging area)
    working tree의 변경사항을 바로 repository로 커밋하지 않는다.
    대신 the index라는 곳에 먼저 등록한다. 커밋하기 전에 변경사항들을 
    하나씩 "확인하는" 역활을 한다고 생각할 수있다. 
    이변 경사항들은 한꺼번에 commit되게 된다.
working tree
    파일 시스템에서 repository를 가지고 있는 디렉토리
    (보통 .git이라는 서브 디렉토리를 포함한다)를 
    working tree라고 한다. 
    working tree는, 이 디렉토리에 있는 모든 파일과 하위 디렉토를
    포함한다.
commit
    커밋은 어느 시점에 working tree의 snapshot이다. 
    커밋을 할때 원래 HEAD였던 commit은, 이 새로운 커밋의 부모가 된다. 
    이 부모자식 관계가 "revision history"라는 개면을 만들게 된다.
tag
    tag또한 commit의 이름이다. branch와 비슷한데, 
    tag은 항상 같은 커밋을 가리킨다는 점이 다르다. 
    그리고 tag 은 설명 문구를 가질수 있다. 


____________________________________________________end ] 
"""
