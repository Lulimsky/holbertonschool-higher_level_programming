#include "lists.h"

/**
 * insert_node - insterts a node in a sorted list
 * @head: pointer to the first node
 * @number: number to sort
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *here = *head;
	listint_t *node = NULL;
	listint_t *aux = NULL;

	if (!head)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		node->next = *head;
		return (*head = node);
	}
	else
	{
		while (here && here->n < number)
		{
			aux = here;
			here = here->next;
		}
		aux->next = node;
		node->next = here;
	}

	return (node);
}
