#include "pch.h"
#include <stdio.h>;
extern "C"
{
	__declspec(dllexport) void foo()
	{
		printf(" \n Hello World");
	}

}
extern "C"
{
	__declspec(dllexport) int Add(int a, int b)
	{
		{
			return a + b;
		}

	}
}

extern "C"
{
	__declspec(dllexport) char* textreturn(const char* phrase, char* result, size_t resultMaxLength)
	{

		{
			_snprintf_s(result, resultMaxLength, _TRUNCATE, "Decorated <%s>", phrase);
			return result;
		}

	}
}
