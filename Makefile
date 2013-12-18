# Makefile for the AVL tree assignment

OBJS = main.o
CC = g++
DEBUG = -g
CFLAGS = -Wall $(DEBUG)
LFLAGS = -Wall $(DEBUG)

main: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o timeTracker

main.o: main.cpp 
	$(CC) -c $(CFLAGS) main.cpp

clean:
	rm -f *.o a.out main timeTracker
