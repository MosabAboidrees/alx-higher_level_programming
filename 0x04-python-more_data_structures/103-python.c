#include <Python.h>

/* Function prototypes */
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 *
 * This function checks if the given PyObject is a bytes object and prints
 * its size and the first 10 bytes as hexadecimal values. If the object is not
 * a valid bytes object, it prints an error message.
 */
void print_python_bytes(PyObject *p)
{
	/* Variable declarations */
	unsigned char idx, size;
	/* Cast the PyObject to a PyBytesObject */
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	/* Verify if the object is a bytes object */
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Print the size of the bytes object and its string representation */
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	/* Determine the number of bytes to print, limited to 10 */
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	/* Print the first 'size' bytes of the byte object */
	printf("  first %d bytes: ", size);
	for (idx = 0; idx < size; idx++)
	{
		printf("%02hhx", bytes->ob_sval[idx]);
		if (idx == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 *
 * This function casts the PyObject to a PyListObject to access
 * specific data fields like size and allocated. It iterates through
 * each item, printing the type and additional bytes info if applicable.
 */
void print_python_list(PyObject *p)
{
	/* Variable declarations */
	int size, alloc_sp, idx;
	const char *type;

	/* Cast the PyObject to a PyListObject */
	PyListObject *list = (PyListObject *)p;
	/* Cast PyObject to PyVarObject to access object size */
	PyVarObject *var = (PyVarObject *)p;

	/* Retrieve and print the size and allocated space of the list */
	size = var->ob_size;
	alloc_sp = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc_sp);
	
	/* Iterate through each item in the list */
	for (idx = 0; idx < size; idx++)
	{
		/* Retrieve the type of each element in the list */
		type = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, type);
		/* Special case: if element is a bytes object, print its bytes info */
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
	}
}
