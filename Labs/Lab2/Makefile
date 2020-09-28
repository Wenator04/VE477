CC = clang
CFLAGS = -std=gnu11 -O2 -Wall 
# -Wextra -Werror -pedantic -Wno-unused-result
LAB2_SRC = main.c MST.c

LAB2 = main
.PHONY: clean

all: $(LAB2) 
	@echo $(LAB2) successfully constructed

$(LAB2): $(LAB2_SRC)
	$(CC) $(CFLAGS) -o $(LAB2) $(LAB2_SRC)

# $(LAB2MC) : $(LAB2_SRC)
# 	$(CC) $(CFLAGS) $(LAB2MC_FLAGS) -o $(LAB2MC) $(LAB2_SRC)

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) *.o *.a *~ $(LAB2) 
	# $(LAB2MC)