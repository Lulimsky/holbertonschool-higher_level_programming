#include "lists.h"
/**
 * insert_node - insterts a node in a sorted list
 * @head: pointer to the first node
 * @number: number to sort
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *aux = *head, *prev;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if (aux->n >= number)
	{
		node->next = aux;
		*head = node;
		return (node);
	}
	while (aux)
	{
		if (aux->n <= number)
		{
			prev = aux;
			aux = aux->next;
		}
		else
			break;
	}
	node->next = aux;
	prev->next = node;
	return (node);
}
