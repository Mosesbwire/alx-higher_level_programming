#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle
  * @list: points to the start of the linked list
  * Return: 0 if there is no cycle otherwise return 1
  */

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	return (0);
}
