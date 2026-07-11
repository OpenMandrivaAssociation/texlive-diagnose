%global tl_name diagnose
%global tl_revision 19387

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A diagnostic tool for a TeX installation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diagnose
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides macros to assist evaluation of the capabilities of a TeX
installation (i.e., what extensions it supports). An example document
that examines the installation is available.

