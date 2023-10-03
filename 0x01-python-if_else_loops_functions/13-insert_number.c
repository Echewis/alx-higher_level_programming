#include "lists.h"
/**
 * *insert_node - this will inserts a number into a linked list
 * @head: this is the head of list
 * @number: it the number to be added
 * Return: it'll return nothing if the code fails else it will return positve
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodez = *head, *fresh;

	fresh = malloc(sizeof(listint_t));
	if (fresh == NULL)
		return (NULL);
	fresh->n = number;

	if (nodez == NULL || nodez->n >= number)
	{
		fresh->next = nodez;
		*head = fresh;
		return (fresh);
	}
	while (nodez && nodez->next && nodez->next->n < number)
		nodez = nodez->next;

	fresh->next = nodez->next;
	nodez->next = fresh;

	return (fresh);
}
