#
# spec file for package obs-api-deps
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           obs-api-deps
Summary:        The Open Build Service -- Gem dependencies
License:        MIT
Group:          Productivity/Networking/Web/Utilities
Version:        2.7.5020140303
Release:        0
Url:            http://en.opensuse.org/Build_Service
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        open-build-service-%version.tar.xz
Source1:        find-requires.sh
BuildRequires:  ruby2.5
BuildRequires:  ruby2.5-rubygem-bundler
%if 0%{?suse_version} < 1210
BuildRequires:  xz
%endif

%description
This package serves one purpose only: to list the dependencies in Gemfile.lock

%package -n obs-api-testsuite-deps
Summary:        The Open Build Service -- The Testsuite dependencies
Group:          Productivity/Networking/Web/Utilities
# dependencies not needed in production
# Requires:       %%(echo `bash %{S:1} %{S:0} "ruby:2.5.0"`)
# expand this to avoid messing about with ^ that
Requires:       rubygem(rake) = 12.3.0, rubygem(concurrent-ruby) = 1.0.5, rubygem(i18n) = 0.9.1, rubygem(minitest) = 5.10.3, rubygem(thread_safe) = 0.3.6, rubygem(tzinfo) = 1.2.4, rubygem(activesupport) = 5.1.4, rubygem(builder) = 3.2.3, rubygem(erubi) = 1.7.0, rubygem(mini_portile2) = 2.3.0, rubygem(nokogiri) = 1.8.2, rubygem(rails-dom-testing) = 2.0.3, rubygem(crass) = 1.0.3, rubygem(loofah) = 2.2.2, rubygem(rails-html-sanitizer) = 1.0.4, rubygem(actionview) = 5.1.4, rubygem(rack) = 2.0.3, rubygem(rack-test) = 0.8.2, rubygem(actionpack) = 5.1.4, rubygem(nio4r) = 2.1.0, rubygem(websocket-extensions) = 0.1.3, rubygem(websocket-driver) = 0.6.5, rubygem(actioncable) = 5.1.4, rubygem(globalid) = 0.4.1, rubygem(activejob) = 5.1.4, rubygem(mini_mime) = 1.0.0, rubygem(mail) = 2.7.0, rubygem(actionmailer) = 5.1.4, rubygem(activemodel) = 5.1.4, rubygem(activemodel-serializers-xml) = 1.0.2, rubygem(arel) = 8.0.0, rubygem(activerecord) = 5.1.4, rubygem(acts_as_list) = 0.9.10, rubygem(acts_as_tree) = 2.7.0, rubygem(public_suffix) = 3.0.1, rubygem(addressable) = 2.5.2, rubygem(airbrake-ruby) = 2.5.0, rubygem(airbrake) = 7.1.0, rubygem(amq-protocol) = 2.3.0, rubygem(annotate) = 2.7.2, rubygem(ansi) = 1.5.0, rubygem(ast) = 2.4.0, rubygem(bcrypt) = 3.1.11, rubygem(uniform_notifier) = 1.10.0, rubygem(bullet) = 5.7.0, rubygem(bunny) = 2.9.1, rubygem(xpath) = 3.0.0, rubygem(capybara) = 2.17.0, rubygem(capybara_minitest_spec) = 1.0.6, rubygem(chunky_png) = 1.3.10, rubygem(cliver) = 0.3.2, rubygem(clockwork) = 2.0.2, rubygem(cocoon) = 1.2.11, rubygem(json) = 2.1.0, rubygem(docile) = 1.1.5, rubygem(simplecov-html) = 0.10.1, rubygem(simplecov) = 0.14.1, rubygem(url) = 0.3.2, rubygem(codecov) = 0.1.10, rubygem(method_source) = 0.9.0, rubygem(thor) = 0.20.0, rubygem(railties) = 5.1.4, rubygem(codemirror-rails) = 5.16.0, rubygem(coderay) = 1.1.2, rubygem(coffee-script-source) = 1.12.2, rubygem(execjs) = 2.7.0, rubygem(coffee-script) = 2.4.1, rubygem(coffee-rails) = 4.2.2, rubygem(colorize) = 0.8.1, rubygem(concurrent-ruby-ext) = 1.0.5, rubygem(safe_yaml) = 1.0.4, rubygem(crack) = 0.4.3, rubygem(cssmin) = 1.0.3, rubygem(daemons) = 1.2.6, rubygem(dalli) = 2.7.6, rubygem(sprockets) = 3.7.1, rubygem(sprockets-rails) = 3.2.1, rubygem(rails) = 5.1.4, rubygem(data_migrate) = 3.2.2, rubygem(database_cleaner) = 1.6.2, rubygem(delayed_job) = 4.1.4, rubygem(delayed_job_active_record) = 4.1.2, rubygem(diff-lcs) = 1.3, rubygem(equatable) = 0.5.0, rubygem(escape_utils) = 1.2.1, rubygem(factory_bot) = 4.8.2, rubygem(factory_bot_rails) = 4.8.2, rubygem(faker) = 1.8.7, rubygem(feature) = 1.4.0, rubygem(ffi) = 1.9.18, rubygem(path_expander) = 1.0.2, rubygem(sexp_processor) = 4.9.0, rubygem(ruby_parser) = 3.9.0, rubygem(flog) = 4.6.1, rubygem(jquery-rails) = 4.3.1, rubygem(flot-rails) = 0.0.7, rubygem(font-awesome-rails) = 4.7.0.2, rubygem(tty-color) = 0.4.2, rubygem(pastel) = 0.7.2, rubygem(refinements) = 4.3.0, rubygem(runcom) = 1.4.0, rubygem(git-cop) = 1.7.1, rubygem(gssapi) = 1.2.0, rubygem(temple) = 0.8.0, rubygem(tilt) = 2.0.8, rubygem(haml) = 5.0.4, rubygem(rainbow) = 2.2.2, rubygem(parallel) = 1.12.0, rubygem(parser) = 2.4.0.2, rubygem(powerpack) = 0.1.1, rubygem(ruby-progressbar) = 1.9.0, rubygem(unicode-display_width) = 1.3.0, rubygem(rubocop) = 0.51.0, rubygem(sysexits) = 1.2.0, rubygem(haml_lint) = 0.27.0, rubygem(hashdiff) = 0.3.7, rubygem(innertube) = 1.1.0, rubygem(joiner) = 0.3.4, rubygem(rb-fsevent) = 0.10.2, rubygem(rb-inotify) = 0.9.10, rubygem(sass-listen) = 4.0.0, rubygem(sass) = 3.5.3, rubygem(sass-rails) = 5.0.7, rubygem(jquery-datatables-rails) = 3.4.0, rubygem(jquery-ui-rails) = 4.2.1, rubygem(kaminari-core) = 1.1.1, rubygem(kaminari-actionview) = 1.1.1, rubygem(kaminari-activerecord) = 1.1.1, rubygem(kaminari) = 1.1.1, rubygem(kgio) = 2.11.0, rubygem(launchy) = 2.4.3, rubygem(metaclass) = 0.0.4, rubygem(middleware) = 0.1.0, rubygem(minitest-fail-fast) = 0.1.0, rubygem(minitest-reporters) = 1.1.19, rubygem(mocha) = 1.3.0, rubygem(momentjs-rails) = 2.17.1, rubygem(mousetrap-rails) = 1.4.6, rubygem(mysql2) = 0.4.10, rubygem(nokogumbo) = 1.5.0, rubygem(rspec-support) = 3.5.0, rubygem(rspec-core) = 3.5.4, rubygem(rspec-expectations) = 3.5.0, rubygem(rspec-mocks) = 3.5.0, rubygem(rspec) = 3.5.0, rubygem(nyan-cat-formatter) = 0.12.0, rubygem(peek) = 1.0.1, rubygem(peek-dalli) = 1.2.0, rubygem(peek-mysql2) = 1.2.0, rubygem(pkg-config) = 1.2.3, rubygem(poltergeist) = 1.17.0, rubygem(power_assert) = 1.1.1, rubygem(pry) = 0.11.3, rubygem(pundit) = 1.1.0, rubygem(rails-controller-testing) = 1.0.2, rubygem(rails_tokeninput) = 1.7.0, rubygem(raindrops) = 0.18.0, rubygem(rantly) = 1.1.0, rubygem(rdoc) = 6.0.1, rubygem(redcarpet) = 3.4.0, rubygem(responders) = 2.4.0, rubygem(riddle) = 2.2.0, rubygem(rspec-rails) = 3.5.2, rubygem(rubocop-rspec) = 1.20.1, rubygem(ruby-ldap) = 0.9.19, rubygem(sanitize) = 4.6.4, rubygem(shoulda-matchers) = 3.1.2, rubygem(single_test) = 0.6.0, rubygem(sprite-factory) = 1.7.1, rubygem(test-unit) = 3.2.7, rubygem(thinking-sphinx) = 3.4.2, rubygem(timecop) = 0.9.1, rubygem(uglifier) = 4.1.5, rubygem(unicorn) = 5.3.0, rubygem(unicorn-rails) = 2.2.1, rubygem(vcr) = 4.0.0, rubygem(voight_kampff) = 1.1.1, rubygem(webmock) = 3.3.0, rubygem(xmlhash) = 1.3.7, rubygem(xmlrpc) = 0.3.0, rubygem(yajl-ruby) = 1.3.1

Requires:       perl-BSSolv >= 0.18.0
# Required by source server
Requires:       createrepo
Requires:       diffutils
Requires:       git-core
Requires:       patch

# needed for api test suite
%if 0%{suse_version} > 1210
Requires:       libxml2-tools
%else
Requires:       libxml2
%endif

Recommends:     yum yum-metadata-parser repoview dpkg
Recommends:     deb >= 1.5
Recommends:     lvm2
Recommends:     openslp-server
Recommends:     obs-signd
Recommends:     inst-source-utils
Requires:       perl-Compress-Zlib
Requires:       perl-File-Sync >= 0.10
Requires:       perl-JSON-XS
Requires:       perl-Net-SSLeay
Requires:       perl-Socket-MsgHdr
Requires:       perl-XML-Parser
Requires:       perl-XML-Simple
Requires:       perl(GD)
Requires:       sphinx >= 2.1.8

%description -n obs-api-testsuite-deps
This is the API server instance, and the web client for the
OBS.

%prep
echo > README <<EOF
This is just a meta package with requires
EOF

%build

%install

# main package is .src.rpm only

%files -n obs-api-testsuite-deps
%defattr(-,root,root)
%doc README

%changelog
