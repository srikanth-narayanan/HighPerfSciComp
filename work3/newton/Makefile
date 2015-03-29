# /Users/Chikoo/GitHub/MyUWHPSC/work3/newton/Makefile

OBJECTS = functions.o newton.o intersections.o
MODULES = functions.mod newton.mod

FFLAGS = -g

.PHONY: intersections clean 

intersections: intersections.exe
	./intersections.exe

intersections.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o intersections.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod

