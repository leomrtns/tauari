#include <Python.h>
#include <biomcmc.h>

static PyObject *TauariError;


static PyObject *
tauari_testfunction (PyObject *self, PyObject *args)
{
  const char *str1, *str2;
  PyObject *arg1, *arg2, *res_tuple;
  double *res_doublevector=NULL; /* output with distances, allocated by library function and freed here */
  int i, n_res = 2;

  if (!PyArg_ParseTuple(args,  "UU", &arg1, &arg2))  return NULL; 
  str1 = PyBytes_AsString(PyUnicode_AsUTF8String(arg1));
  str2 = PyBytes_AsString(PyUnicode_AsUTF8String(arg2));

  biomcmc_random_number_init (0ULL);
  printf ("I got [%s] and [%s] \n rng = %d", str1, str2, biomcmc_rng_get_algorithm()); // DEBUG
  //if (error) { PyErr_SetString(TauariError, "gene and species trees can't be compared"); return NULL; }
  biomcmc_rng_set_algorithm (9);
  res_tuple = PyTuple_New(n_res);
  for (i = 0; i < n_res; i++) PyTuple_SetItem(res_tuple, i, PyLong_FromUnsignedLongLong ( biomcmc_rng_get() ));

  return res_tuple;
}

static PyObject *
tauari_test2 (PyObject *self, PyObject *args)
{
  printf ("and now rng = %d", biomcmc_rng_get_algorithm()); // DEBUG
  return ;
}

PyMODINIT_FUNC
PyInit__tauari_c (void) /* it has to be named PyInit_<module name in python> */
{
  PyObject *m;
  static PyMethodDef TauariMethods[] = {
     {"testfunction", (PyCFunction) tauari_testfunction, METH_VARARGS, 
      "receives two strings, returns magic numbers."},
     {"test2", (PyCFunction) tauari_test2, METH_VARARGS, "check global"},
     {NULL, NULL, 0, NULL}        /* Sentinel */
  };
  PyDoc_STRVAR(tauari__doc__,"lowlevel functions in C for treesignal module");

  static struct PyModuleDef tauarimodule = { PyModuleDef_HEAD_INIT, "tauari_c", tauari__doc__, -1, TauariMethods};

  m = PyModule_Create(&tauarimodule);
  if (m == NULL) return NULL;

  TauariError = PyErr_NewException("__tauari_c.error", NULL, NULL);
  Py_INCREF(TauariError);
  PyModule_AddObject(m, "error", TauariError);
  return m;
}

int
main (int argc, char *argv[])
{
  wchar_t *program = Py_DecodeLocale(argv[0], NULL);
  if (program == NULL) { fprintf(stderr, "Fatal error: cannot decode argv[0]\n"); exit(1); }
  
  PyImport_AppendInittab("_tauari_c", PyInit__tauari_c); /* Add a built-in module, before Py_Initialize */
  Py_SetProgramName(program); /* Pass argv[0] to the Python interpreter */
  Py_Initialize(); /* Initialize the Python interpreter.  Required. */
 
  PyMem_RawFree(program);
  return 0;
} 
