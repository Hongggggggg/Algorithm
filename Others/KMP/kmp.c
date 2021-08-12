#include <stdio.h>
#include <string.h>
#include <time.h>
#include <windows.h>

char str[] = {"abcdefabcdeabcdeg"}; 
char tar_str[] = {"abababca"};


int Brute_Force(char* all_string, char* target_str)
{
    printf("Str: %s\r\n", all_string);
    printf("Tar: %s\r\n", target_str);

    int i = 0, j = 0;

    while(i < strlen(all_string) && j < strlen(target_str))
    {
        if(all_string[i] == target_str[j])
        {
            printf("same: str[%d]: %c, tar[%d]: %c\r\n", i, all_string[i], j, target_str[j]);
            i++;
            j++;
        }
        else
        {
            printf("unsame: str[%d]: %c, tar[%d]: %c\r\n", i, all_string[i], j, target_str[j]);
            i = i - j + 1;
            j = 0;
        }
        
    }
    return (j == strlen(target_str)) ? (i - j) : -1;
}


void getNext(char * p, int * next)
{
	next[0] = -1;
	int i = 0, j = -1;

	while (i < strlen(p))
	{
		if (j == -1 || p[i] == p[j])
		{
			++i;
			++j;
			next[i] = j;
		}	
		else
        {
            j = next[j];
        }
        printf("i: %d, j: %d, next[%d]: %d\r\n", i, j, i, next[i]);
	}
}


void main(void)
{
    DWORD start_time = GetTickCount();

    //int pos = Brute_Force(str, tar_str);

    DWORD end_time = GetTickCount();

    //printf("start: %d, end %d, time: %d\r\n", start_time, end_time, end_time - start_time);

    //printf("Pos: %d\r\n", pos);

    int next[8];

    getNext(tar_str, next);
}
