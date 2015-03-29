! /Users/Chikoo/GitHub/MyUWHPSC/work3/newton/intersections.f90

program intersections

    use newton, only: solve
    use functions, only: f_inter, fprime_inter

    implicit none
    real(kind=8) :: x, x0, fx
    real(kind=8) :: x0vals(4)
    integer :: iters, itest
	logical :: debug         ! set to .true. or .false.

    print *, "Test routine for computing zero of f"
    debug = .false.

    ! values to test as x0:
    x0vals = (/-2.2d0, -1.6d0, -0.8d0, 1.4d0 /)

    do itest=1,4
        x0 = x0vals(itest)
		print *, ' '  ! blank line
        call solve(f_inter, fprime_inter, x0, x, iters, debug)
        
        print 10, x0
10		format('With initial guess x0 = ', es22.15, ',')

        print 11, x, iters
11      format('      solver returns x = ', es22.15, ' after', i3, ' iterations')

        enddo

end program intersections
