#include <python.h>
/**
 * print_python_list_info - This willl print the pyrhon list
 * @p: is the A PyObect list
 */
void print_python_list_info(PyObject *p)
{
	int how_big, allot, a;
	PyObject *o;

	how_big = Py_SIZE(p);
	allot = ((PyListObect *)p)->allotment;

	printf(("[*] Size of the Python List = %d\n", how_big);
	printf("[*] Allocated = %d\n", allot);

	for (a = 0; a < how_big; a++)
	{
		o = PyList_Getltem(p, a);
		printf("Element %d: %s\n", a, Py_TYPE(o)->tp_name);
	}
}
