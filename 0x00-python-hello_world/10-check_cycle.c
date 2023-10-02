#include "lists.h"

/**
 * check_cycle - This function checks if a singly link list has a cycle
 * @list: is the first node
 * Return: will return 0 if the list is empty and one if the list is not empty
 */
int check_cycle(listint_t *list)
{
	listint_t *new, *look;

	if (list == NULL || list->next == NULL)
		return (0);
	new = list;
	look = new->next;

	while (new != NULL && look->next != NULL
			&& look->next->next != NULL)
	{
		if (new == look)
			return (1);
		new = new->next;
		look = look->next->next;
	}
	return (0);
}
