%global tl_name lua-typo
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.88
Release:	%{tl_revision}.1
Summary:	Highlighting typographical flaws with LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/lua-typo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-typo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prints the list of pages on which typographical flaws were found (i.e.
widows, orphans, hyphenated words split across two pages, consecutive
lines ending with hyphens, paragraphs ending on too short or nearly full
lines, homeoarchy, etc). Customisable colours are used to highlight
these flaws.

