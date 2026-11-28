CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra

TARGET = t08_05_e2663 t08_07_e2664 t08_08_e972 t09_05_e4037 t09_04_e2321

all: $(TARGET)

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)
