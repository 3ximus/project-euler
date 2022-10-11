package lib

import (
	"testing"
)

var target = 20000;

func BenchmarkBasic(b *testing.B) {
	for i := 0; i < b.N; i++ {
		basic(target);
	}
}

func BenchmarkHalved(b *testing.B) {
	for i := 0; i < b.N; i++ {
		halved(target);
	}
}

func BenchmarkThirds(b *testing.B) {
	for i := 0; i < b.N; i++ {
		thirds(target);
	}
}
