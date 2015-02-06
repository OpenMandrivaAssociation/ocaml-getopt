%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Command line parsing a la GNU getopt
Name:		ocaml-getopt
Version:	20120615
Release:	2
License:	MIT
Group:		Development/Other
Url:		http://forge.ocamlcore.org/projects/ocaml-getopt/
Source0:	http://forge.ocamlcore.org/frs/download.php/896/ocaml-getopt-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
The OCaml distribution comes with the module Arg specialized in command-line
parsing. However, it doesn't support the well known features of GNU getopt
and getopt_long.

The module Getopt is an alternative; it supports GNU syntax, but from the
programmer point of view, it is close to the spirit of Arg: the programmer
gives to the general parsing function a list of possible options, together
with the behavior of these options.

%files
%doc COPYING Changes README
%dir %{_libdir}/ocaml/getopt
%{_libdir}/ocaml/getopt/META
%{_libdir}/ocaml/getopt/*.cma
%{_libdir}/ocaml/getopt/*.cmi
%{_libdir}/ocaml/getopt/*.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc/
%doc sample.ml
%{_libdir}/ocaml/getopt/*.a
%{_libdir}/ocaml/getopt/*.cmxa
%{_libdir}/ocaml/getopt/*.cmx
%{_libdir}/ocaml/getopt/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n ocaml-getopt

%build
./configure \
    --prefix %{_prefix} \
    --libdir %{_libdir} \
    --libexecdir %{_libexecdir} \
    --exec-prefix %{_exec_prefix} \
    --bindir %{_bindir} \
    --sbindir %{_sbindir} \
    --mandir %{_mandir} \
    --datadir %{_datadir} \
    --localstatedir %{_localstatedir} \
    --sharedstatedir %{_sharedstatedir} \
    --destdir %{buildroot}

make all
make doc
mv doc.docdir doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/getopt
make install
cp getopt.mli $OCAMLFIND_DESTDIR/getopt

