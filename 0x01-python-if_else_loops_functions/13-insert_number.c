#include "lists.h"
#include <stdlib.h>
/**
  * insert_node - inserts a node in a sorted singly linked list
  * @head: points to pointer to start of list
  * @number: integer data for new node
  * Return: NULL on failure otherwise pointer to inserted node
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *tracker;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	tracker = current->next->next
	if (current->n > current->next->n)
	{
		while (current->n > number)
		{
			if (tracker->n < number)
			{
				break;
			}
			current = current->next;
			tracker = tracker->next;
		}
	} else
	{
		while (current->n < number)
		{
			if (tracker->n > number)
			{
				break;
			}
			current = current->next;
			tracker = tracker->next;
		}
	}
	new_node->next = tracker;
	current->next = new_node;
	return (new_node);
}
