! /Users/Chikoo/GitHub/MyUWHPSC/work3/problem7/functions.f90

module functions
	
	! Module parameters
	real(kind=8) :: ephi
    save

contains

!!!!!!!!!!!!!!!!!!!!function containing  f(x)=(x−1)4−ϵ !!!!!!!!!!!!!!!!!!!!!!!!!!

real(kind=8) function f_quartic(x)
	implicit none
	real(kind=8), intent(in) :: x
	
	f_quartic = ((x - 1) ** 4 ) - ephi

end function f_quartic

!!!!!!!!!!!!!function containing  derivative of f(x)=(x−1)4−ϵ  !!!!!!!!!!!!!!!!!!

real(kind=8) function fprime_quartic(x)
	implicit none
	real(kind=8), intent(in) :: x
	
	fprime_quartic = (4 * x ** 3) - (12 * x ** 2) + (12 * x) - 4

end function fprime_quartic

!!!!!!!!!!!!!!!!!!!!function containing g1(x) - g2(x)!!!!!!!!!!!!!!!!!!!!!!!!!!!!

real(kind=8) function f_inter(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    ! declare local variables
    real(kind=8) :: pi
	
	pi = 4. * atan(1.)
    f_inter = x * cos(pi * x) - (1 - (0.6 * x ** 2))

end function f_inter

!!!!!!!!!!!!!!!!!!!!function derivative of f_inter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

real(kind=8) function fprime_inter(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    ! declare local variables
    real(kind=8) :: pi
    
    pi = 4. * atan(1.)
    fprime_inter = (-x * pi) * sin(pi * x) + cos(pi * x) + 1.2 * x

end function fprime_inter

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! square root function !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt

!!!!!!!!!!!!!!!!!!!!!!! derivative of square root function !!!!!!!!!!!!!!!!!!!!!!!

real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt

end module functions