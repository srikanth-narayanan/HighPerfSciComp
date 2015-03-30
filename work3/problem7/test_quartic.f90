! /Users/Chikoo/GitHub/MyUWHPSC/work3/problem7/test_quartic.f90

program test_quartic

    use newton, only: solve, tol
    use functions, only: f_quartic, fprime_quartic, ephi

    implicit none
    real(kind=8) :: x, x0, fx, xstar
    real(kind=8) :: mytol(3), myephi(3)
    integer :: iters, itol, iephi
	logical :: debug         ! set to .true. or .false.

    debug = .false.

    ! values to test as x0:
    x0 = 4.0d0
    
    ! set tolerance and epsilon
    mytol = (/1.0d-5, 1.0d-10, 1.0d-14/)
    myephi = (/1.0d-4, 1.0d-8, 1.0d-12/)
    
    print 10, x0
10	format('With initial guess x0 = ', es22.15, ',')
	print *, ' '  ! blank line
	print *, '    epsilon        tol    iters          x                 f(x)        x-xstar'
	
    do iephi=1,3
    	do itol=1,3
    		tol = mytol(itol)
    		ephi = myephi(iephi)
			call solve(f_quartic, fprime_quartic, x0, x, iters, debug)
			
			fx = f_quartic(x)
			xstar = 1.1d0
			print 11, ephi, tol, iters, x, fx, x-xstar
11 			format(2es13.3, i4, es24.15, 2es13.3)
			
        enddo
        print *, ' '  ! blank line
    enddo

end program test_quartic
