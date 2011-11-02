Name:		texlive-diagnose
Version:	0.2
Release:	1
Summary:	A diagnostic tool for a TeX installation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagnose
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides macros to assist evaluation of the capabilities of a
TeX installation (i.e., what extensions it supports). An
example document that examines the installation is available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
