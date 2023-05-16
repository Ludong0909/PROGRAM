PROGRAM PREVIEW
IMPLICIT NONE
INTEGER, PARAMETER :: MAX = 10
INTEGER :: i
REAL, DIMENSION(MAX) :: a = (/(REAL(i*2), i=1,10)/)
REAL, DIMENSION(MAX/2) :: b
write(*,*) a(4:8)
b = Log(a(4:8))
write(*,*) a
write(*,*) b(3:4)
END PROGRAM PREVIEW