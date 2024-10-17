Name:		texlive-courier-scaled
Version:	24940
Release:	2
Summary:	Provides a scaled Courier font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/psfonts/courier-scaled
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
