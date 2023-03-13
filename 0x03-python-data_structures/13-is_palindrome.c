#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_length - gets length of list
 * @head: points to start of list
 * Return: length of list
 */

int list_length(listint_t *head)
{
	listint_t *temp_head = head;
	int length = 0;

	if (head == NULL)
		return (0);

	while (temp_head != NULL)
	{
		length += 1;
		temp_head = temp_head->next;
	}

	return (length);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer pointing to start of list
 * Return: 1 if is palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int length = list_length(*head);
	int x, y, loop_var;
	int *container;
	listint_t *temp;

	if (*head == NULL)
	{
		return (1);
	}

	container = malloc(sizeof(int) * length);

	if (container == NULL)
		exit(1);

	temp = *head;
	x = 0;
	while (temp != NULL)
	{
		container[x] = temp->n;
		temp = temp->next;
		x++;
	}

	loop_var = length / 2;

	for (y = 0; y < loop_var; y++)
	{
		if (container[y] != container[(length - 1) - y])
			return (0);
	}
	
	free(container);
	return (1);
}
