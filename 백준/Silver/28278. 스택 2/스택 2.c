#include <stdio.h>
#include <stdlib.h>

typedef int Data;
typedef enum { false, true } bool; // 수정: false와 true를 대문자로 변경
#define MAX_STACK 1000000

typedef struct {
    Data items[MAX_STACK];
    int top;
} Stack1;

void InitStack(Stack1 *pstack);
bool IsFull(Stack1 *pstack);
bool IsEmpty(Stack1 *pstack);
void Push(Stack1 *pstack, Data num);
void Pop(Stack1 *pstack);
void Peek(Stack1 *pstack);

int main() {

    int n;
    scanf("%d", &n);
    Stack1 stack;

    InitStack(&stack);
    int inp;
    Data inp1;

    for (int i = 0; i < n; i++) {
        scanf("%d", &inp);

        switch (inp) {
            case 1:
                scanf("%d", &inp1);
                Push(&stack, inp1);
                break;
            case 2:
                Peek(&stack);
                Pop(&stack);
                break;
            case 3:
                printf("%d\n", stack.top+1); // 수정: 개행 문자('\n') 추가
                break;
            case 4:
                if (IsEmpty(&stack)) {
                    printf("1\n"); // 수정: 개행 문자('\n') 추가
                } else {
                    printf("0\n"); // 수정: 개행 문자('\n') 추가
                }
                break;
            case 5:
                Peek(&stack);
                break;
        }
    }
}

void InitStack(Stack1 *pstack) {
    pstack->top = -1;
}

bool IsFull(Stack1 *pstack) {
    return pstack->top == MAX_STACK - 1;
}

bool IsEmpty(Stack1 *pstack) {
    return pstack->top == -1;
}

void Push(Stack1 *pstack, Data num) {
    if (IsFull(pstack)) {
        exit(1);
    }
    pstack->items[++(pstack->top)] = num;
}

void Pop(Stack1 *pstack) {
    if (!IsEmpty(pstack)) {
        --(pstack->top);
    }
}

void Peek(Stack1 *pstack) {
    if (IsEmpty(pstack)) {
        printf("%d\n", -1); // 수정: 개행 문자('\n') 추가
    } else {
        printf("%d\n", pstack->items[pstack->top]); // 수정: 개행 문자('\n') 추가
    }
}
