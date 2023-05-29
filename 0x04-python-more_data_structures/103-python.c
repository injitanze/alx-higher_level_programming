#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information.
 *
 * @p: Python Object.
 * Return: No return.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, z, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying str: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (z = 0; z < limit; z++)
		if (str[z] >= 0)
			printf(" %02x", str[z]);
		else
			printf(" %02x", 256 + str[z]);

	printf("\n");
}

/**
 * print_python_list - Prints list information.
 *
 * @p: Python Object.
 * Return: No return.
 */
void print_python_list(PyObject *p)
{
	long int size, z;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (z = 0; z < size; z++)
	{
		obj = ((PyListObject *)p)->ob_item[z];
		printf("Element %ld: %s\n", z, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
