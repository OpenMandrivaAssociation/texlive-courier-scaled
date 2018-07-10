# revision 24940
# category Package
# catalog-ctan /fonts/psfonts/courier-scaled
# catalog-date 2011-12-25 01:31:26 +0100
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-courier-scaled
Version:	20180303
Release:	2
Summary:	Provides a scaled Courier font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/psfonts/courier-scaled
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package sets the default typewriter font to Courier with a
possible scale factor (in the same way as the helvet package
for Helvetica works for sans serif).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/courier-scaled/8rpcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/couriers.sty
%{_texmfdistdir}/tex/latex/courier-scaled/il2pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/ly1pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/omlpcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/omspcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/ot1pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/t1pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/t5pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/ts1pcrs.fd
%{_texmfdistdir}/tex/latex/courier-scaled/xl2pcrs.fd
%doc %{_texmfdistdir}/doc/fonts/courier-scaled/Couriers.pdf
%doc %{_texmfdistdir}/doc/fonts/courier-scaled/Couriers.tex
%doc %{_texmfdistdir}/doc/fonts/courier-scaled/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111225-1
+ Revision: 758858
- Update to latest upstream release

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070320-3
+ Revision: 750557
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070320-2
+ Revision: 745205
- texlive-courier-scaled

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070320-1
+ Revision: 718157
- texlive-courier-scaled
- texlive-courier-scaled
- texlive-courier-scaled
- texlive-courier-scaled

