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
	listint_t *new_node, *current;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if (current->n > current->next->n)
	{
		while (current->next != NULL)
		{
			if (current->n >= number && current->next->n <= number)
			{
				break;
			}
			current = current->next;
		}
	} else
	{
		while (current->next != NULL)
		{
			if (current->n <= number && current->next->n >= number)
			{
				break;
			}
			current = current->next;
		}
	}
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
