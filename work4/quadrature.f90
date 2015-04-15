! /Users/Chikoo/GitHub/MyUWHPSC/quadrature.f90

module quadrature

	! module parameters

contains

subroutine trapezoid(f,a,b,n,int_trapz)

	! Estimate the integral of function using trapezoidal rule
	! Input:
	! 	f: input function for which integral is calculated
	!	a: lower limit for the integral
	!	b: upper limit for the integral
	!	n: number of points between a and b
	! Output:
	!	int_trapz: Return the definite integral of the given function
	
	implicit none
	real (kind=8), external :: f
	real (kind=8), intent(in) :: a, b
	integer, intent(in) :: n
	real (kind=8), intent(out) :: int_trapz
	
	! Local variables used
	real (kind=8) :: xj(n), fj(n)
	integer :: ii
	real (kind=8) :: h
	
	h = (b - a) / (n - 1)
	
	! Calculate list of X
	call linspace(a,b,n,xj)
	
	! Calculate function values
	do ii = 1,n
		fj(ii) = f(xj(ii))
		end do
	
	int_trapz = h * SUM(fj) - 0.5 * h * (fj(1) + fj(n))
	
end subroutine trapezoid

subroutine error_table(f, a, b, nvals, int_true)

	! A subroutine to perform convergence test on the trapezoid rule
	! Input:
	! 	f: input function for which integral is calculated
	!	a: lower limit for the integral
	!	b: upper limit for the integral
	!	nvals: 1-d array of values to test
	!	int_true: Real value to check for convergence
	
	implicit none
	real (kind=8), external :: f
	real (kind=8), intent(in) :: a, b, int_true
	integer, dimension(:), intent(in) :: nvals
	
	! local variables
	integer :: kk
	real (kind=8) :: int_trap, last_error, error, ratio
	
	last_error = 0.d0
	
	print *, "    n         trapezoid            error       ratio"
	do kk = 1, size(nvals)
		call trapezoid(f, a, b, nvals(kk), int_trap)
		error = abs(int_trap - int_true)
		ratio = last_error / error
		last_error = error
		print 11, nvals(kk), int_trap, error, ratio
11		format(i8, es22.14, es13.3, es13.3)
		end do

end subroutine error_table

subroutine linspace(x_start, x_end, x_len, x_out)

	! creates a 1-d array with evenly spaced elements
	! Input:
	!	x_start: starting value of the array
	!	x_end: end value of the array
	!	x_len: length of the array needed
	! Output:
	!	x_out: evenly space 1-d array
	
	implicit none
	real (kind=8), intent(in) :: x_start, x_end
	integer, intent(in) :: x_len
	real (kind=8), dimension(:), intent(out) :: x_out
	
	! local variables
	integer :: i
	real :: dx
	
	dx = (x_end - x_start) / (x_len - 1)
	x_out(1) = x_start
	do i = 2, x_len
		! calculate each variable
		x_out(i) = x_out(1) + (i-1) * dx
		end do

end subroutine linspace

end module quadrature