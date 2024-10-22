CC = gcc
CFLAGS = -Wall -g
LIBS = -lcheck -lm -lpthread -lrt -lsubunit
INCLUDES = -I. -I../include

TEST_SRCS = $(wildcard test_*.c)
TEST_OBJS = $(TEST_SRCS:.c=.o)
TEST_BINS = $(TEST_SRCS:.c=)

.PHONY: all clean test debug

all: debug $(TEST_BINS)

debug:
	@echo "Test sources: $(TEST_SRCS)"
	@echo "Test objects: $(TEST_OBJS)"
	@echo "Test binaries: $(TEST_BINS)"

test: $(TEST_BINS)
	for test in $(TEST_BINS); do ./$$test; done

%: %.o
	@echo "Linking $@"
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

%.o: %.c
	@echo "Compiling $<"
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(TEST_OBJS) $(TEST_BINS)
