Client API
==========

The client does not yet implement the complete Web Services-Management
protocol. You can find the currently supported methods here.


WS-Enumeration
--------------

enumerate
~~~~~~~~~
Executes enumerate operation over WSMan and returns an ``lxml.etree.Element``
object of the response received.

Required parameters:

* ``resource_uri``: URI of resource to enumerate.

Optional parameters:

* ``optimization``: flag to enable enumeration optimization. If disabled, the
  enumeration returns only an enumeration context. Defaults to ``True``.

* ``max_elems``: maximum number of elements returned by the operation. Defaults
  to ``100``.

* ``auto_pull``: flag to enable automatic pull on the enumeration context,
  merging the items returned. Defaults to ``True``.

* ``filter_query``: filter query string.

* ``filter_dialect``: filter dialect. Valid options are: ``cql`` and ``wql``.
  Defaults to ``cql``.

pull
~~~~
Executes pull operation over WSMan and returns an ``lxml.etree.Element``
object of the response received.

Required parameters:

* ``resource_uri``: URI of resource to pull.

* ``context``: enumeration context.

Optional parameters:

* ``max_elems``: maximum number of elements returned by the operation. Defaults
  to ``100``.


Custom Actions
---------------

invoke
~~~~~~
Executes custom action over WSMan and returns an ``lxml.etree.Element``
object of the response received.

Required parameters:

* ``resource_uri``: URI of resource to invoke.

* ``method``: name of the method to invoke.

* ``selector``: dictionary of selectors.

* ``properties``: dictionary of properties.
