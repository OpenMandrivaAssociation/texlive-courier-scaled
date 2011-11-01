Name:		texlive-courier-scaled
Version:	20070320
Release:	1
Summary:	Provides a scaled Courier font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/psfonts/courier-scaled
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier-scaled.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package sets the default typewriter font to Courier with a
possible scale factor (in the same way as the helvet package
for Helvetica works for sans serif).

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
%doc %{_texmfdistdir}/doc/latex/courier-scaled/Couriers.pdf
%doc %{_texmfdistdir}/doc/latex/courier-scaled/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
