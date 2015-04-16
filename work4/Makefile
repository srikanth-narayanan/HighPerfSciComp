# /Users/Chikoo/GitHub/MyUWHPSC/Makefile

OBJECTS = quadrature.o test2.o
MODULES = quadrature.mod

FFLAGS = -g

.PHONY: test2 clean 

test2: test2.exe
	./test2.exe

test2.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test2.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod
