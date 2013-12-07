# revision 19387
# category Package
# catalog-ctan /macros/latex/contrib/diagnose
# catalog-date 2006-12-17 18:48:45 +0100
# catalog-license gpl
# catalog-version 0.2
Name:		texlive-diagnose
Version:	0.2
Release:	5
Summary:	A diagnostic tool for a TeX installation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagnose
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagnose.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 750953
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718226
- texlive-diagnose
- texlive-diagnose
- texlive-diagnose
- texlive-diagnose

