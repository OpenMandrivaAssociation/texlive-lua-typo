Name:		texlive-lua-typo
Version:	59457
Release:	2
Summary:	Highlighting typographical flaws with LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lua-typo
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package tracks common typographic flaws in LuaLaTeX
documents, especially widows, orphans, hyphenated words split
over two pages, consecutive lines ending with hyphens,
paragraphs ending on too short lines, etc. Customisable colours
are used to highlight these flaws, and the list of pages on
which typographical flaws were found is printed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/lua-typo
%{_texmfdistdir}/tex/lualatex/lua-typo
%doc %{_texmfdistdir}/doc/lualatex/lua-typo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
