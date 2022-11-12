Name:		texlive-diagnose
Version:	19387
Release:	1
Summary:	A diagnostic tool for a TeX installation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagnose
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides macros to assist evaluation of the capabilities of a
TeX installation (i.e., what extensions it supports). An
example document that examines the installation is available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/diagnose/diagnose.sty
%doc %{_texmfdistdir}/doc/latex/diagnose/INSTALL
%doc %{_texmfdistdir}/doc/latex/diagnose/README
%doc %{_texmfdistdir}/doc/latex/diagnose/diagnose.pdf
%doc %{_texmfdistdir}/doc/latex/diagnose/diagnose.tex
%doc %{_texmfdistdir}/doc/latex/diagnose/mls-diag.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
