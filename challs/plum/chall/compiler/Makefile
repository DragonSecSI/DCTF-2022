CXX=clang++
CXXFLAGS=-std=c++17 -Iinc -O0
CXXLIBS=
OBJS=tokenizer.o grammar.o nodes.o asm.o
BIN=compiler

all: main

main: src/main.cpp ${OBJS}
	${CXX} -o ${BIN} ${CXXFLAGS} $< obj/*.o ${CXXLIBS}

tokenizer.o: src/tokenizer/tokenizer.cpp
	mkdir -p obj
	${CXX} -c -o obj/$@ ${CXXFLAGS} $< ${CXXLIBS}

grammar.o: src/grammar/grammar.cpp
	mkdir -p obj
	${CXX} -c -o obj/$@ ${CXXFLAGS} $< ${CXXLIBS}

nodes.o: src/nodes/nodes.cpp
	mkdir -p obj
	${CXX} -c -o obj/$@ ${CXXFLAGS} $< ${CXXLIBS}

asm.o: src/asm/asm.cpp
	mkdir -p obj
	${CXX} -c -o obj/$@ ${CXXFLAGS} $< ${CXXLIBS}

clean:
	rm -rf obj
	rm -f ${BIN}
