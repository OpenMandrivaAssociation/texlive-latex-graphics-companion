# revision 15878
# category Package
# catalog-ctan /info/examples/lgc
# catalog-date 2006-03-09 14:57:21 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-graphics-companion
Version:	20060309
Release:	1
Summary:	Examples from The LaTeX Graphics Companion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/lgc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-companion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-companion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The source of the examples printed in the book, together with
necessary supporting files.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-10.pic
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-11.pic
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/1-4-9.pic
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-1-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-1-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-1-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-1-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-1-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/10-5-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/11-3-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/11-6-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-1.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-2.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-3.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-4.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/12-0-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-10.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-11.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-12.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-13.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-14.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-15.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-16.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-17.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-18.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-19.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-20.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-2-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-13.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-14.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-15.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-16.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-17.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/2-3-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-1.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-2.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-3.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-4.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-5.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-6.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-7.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-8.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-1-9.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-2-1.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-2-2.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-2-3.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-1.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-10.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-11.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-12.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-13.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-14.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-15.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-16.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-17.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-18.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-19.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-2.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-3.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-4.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-5.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-6.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-7.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-8.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-3-9.mp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/3-4-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-10-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-2-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-2-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-2-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-2-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-2-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-3-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-3-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-10.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-11.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-12.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-4-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-10.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-11.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-12.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-13.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-14.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-15.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-16.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-5-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-10.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-11.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-12.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-13.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-14.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-15.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-16.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-17.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-18.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-19.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-20.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-21.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-22.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-23.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-24.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-25.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-26.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-27.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-28.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-29.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-30.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-31.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-32.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-33.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-34.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-35.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-36.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-37.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-38.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-39.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-40.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-41.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-42.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-43.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-44.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-45.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-46.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-6-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-7-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-7-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-7-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-7-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-8-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-8-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-8-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-8-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-8-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-9-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-9-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/4-9-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-2-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-3-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-4-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-4-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-4-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-4-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-13.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-14.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-15.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-16.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-17.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-18.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-19.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-20.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-21.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-22.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-23.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-24.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-25.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-26.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-27.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-28.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-29.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-30.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-31.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-32.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-33.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-34.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-35.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/5-5-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-13.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-14.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-15.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-16.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-17.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-18.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-19.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-20.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-21.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-22.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-23.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-24.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-2-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-10.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-11.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-12.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-13.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-14.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-3-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-4-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-4-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-4-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-5-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-6-7.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-1.m4
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-2.m4
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-3.m4
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/6-7-4.m4
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-1.mx1
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-1.mx2
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-1.ptx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-5.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-2-6.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-1.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-3.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-4.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-5.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-6.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-7.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-8.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-3-9.abc
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-1.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-10.mx1
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-10.mx2
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-10.ptx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-2.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-3.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-4.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-5.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-6.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-7.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-8.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/7-4-9.mpp
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-1-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-1-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-1-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-1-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-2-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-2-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-2-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-3-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-3-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-3-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-4-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-4-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-5-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-6-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-1.acr
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-1.dwn
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-1.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-2.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-3.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/8-7-4.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-8.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-2-9.ltx
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-10.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-11.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-12.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-13.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-14.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-15.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-16.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-17.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-18.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-19.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-2.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-20.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-3.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-4.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-5.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-6.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-7.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-8.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/9-3-9.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/A-1-1.inl
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/Makefile
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/README
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/ages.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/bar.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/chap.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/clef.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/config.ps.gz
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/decade.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/feature.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/graves.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/inputs/graphics.cfg
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/inputs/header.tex
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/inputs/mfpic.sty
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/inputs/ppex.cls
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/key.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/langs.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/langs2.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/langs3.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/macro.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/mpp.tex
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/note.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/notecc.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/pot.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/script.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/scriptcc.ini
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/stones.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/students.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/veracx.mx1
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/veracx.tex
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/yearm.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/years.dat
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/years.men
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/years.wom
%doc %{_texmfdistdir}/doc/latex/latex-graphics-companion/yearw.dat
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
