require 'activexml/activexml'

class DetailsLogger
  def initialize
    @summary = Hash.new
  end

  def summary!
    ret = @summary
    @summary = Hash.new
    return ret
  end

  def add(d)
    d.each do |key,value|
      key = "api-#{key}"
      if value
	if @summary[key].nil?
          @summary[key] = value
	else
	  @summary[key] += value
	end
      end
    end
  end
end

map = ActiveXML::setup_transport_api(CONFIG['frontend_protocol'], CONFIG['frontend_host'], CONFIG['frontend_port'])

    map.connect :webuiproject, 'rest:///source/:name/_meta?:view',
      :all    => 'rest:///source/',
      :delete => 'rest:///source/:name?:force',
      :issues => 'rest:///source/:name?view=issues'
    map.connect :package, 'rest:///source/:project/:name/_meta?:view',
      :all    => 'rest:///source/:project',
      :issues => 'rest:///source/:project/:name?view=issues'

    map.connect :tagcloud, 'rest:///tag/tagcloud?limit=:limit',
      :alltags  => 'rest:///tag/tagcloud?limit=:limit',
      :mytags => 'rest:///user/:user/tags/_tagcloud?limit=:limit',
      :hierarchical_browsing => 'rest:///tag/tagcloud?limit=:limit'

    map.connect :tag, 'rest:///user/:user/tags/:project/:package',
      :tags_by_object => 'rest:///source/:project/:package/_tags'

    map.connect :webuigroup, 'rest:///group/:title',
      :all => 'rest:///group/'
    map.connect :owner, 'rest:///search/owner?:binary&:devel&:limit&:project&:attribute'
    map.connect :reverseowner, 'rest:///search/owner?:user&:devel&:limit&:project&:attribute'

    map.connect :userchangepasswd, 'rest:///person/changepasswd'

    map.connect :architecture, 'rest:///architectures/:name', :all => 'rest:///architectures/',
                :available => 'rest:///architectures?available=1'
    map.connect :issuetracker, 'rest:///issue_trackers/:name', :all => 'rest:///issue_trackers/'
    map.connect :issue, 'rest:///issue_trackers/:tracker/issues/:name', :all => 'rest:///issue_trackers/:tracker/issues'

    map.connect :wizard, 'rest:///source/:project/:package/_wizard?:response'

    map.connect :directory, 'rest:///source/:project/:package?:expand&:rev'
    map.connect :link, 'rest:///source/:project/:package/_link'
    map.connect :service, 'rest:///source/:project/:package/_service',
                :all => 'rest:///service'
    map.connect :file, 'rest:///source/:project/:package/:filename?:expand&:rev'
    map.connect :jobhislist, 'rest:///build/:project/:repository/:arch/_jobhistory?:limit&:code'

    map.connect :buildresult, 'rest:///build/:project/_result?:view&:package&:code&:lastbuild&:arch&:repository'
    map.connect :fileinfo, 'rest:///build/:project/:repository/:arch/:package/:filename?:view'
    map.connect :statistic, 'rest:///build/:project/:repository/:arch/:package/_statistics'

    map.connect :result, 'rest:///result/:project/:platform/:package/:arch/result'
    map.connect :packstatus, 'rest:///result/:project/packstatus?:command'

    map.connect :collection, 'rest:///search/:what?match=:predicate',
      :id => 'rest:///search/:what/id?match=:predicate',
      :tag => 'rest:///tag/:tagname/:type',
      :tags_by_user => 'rest:///user/:user/tags/:type',
      :hierarchical_browsing => 'rest:///tag/browsing/_hierarchical?tags=:tags'

    map.connect :bsrequest, 'rest:///request/:id', :create => 'rest:///request?cmd=create'

    map.connect :packageattribute, 'rest:///search/attribute?:namespace&:name&:project'
 
    map.connect :attribute, 'rest:///source/:project/:package/_attribute/:attribute',
      :project => 'rest:///source/:project/_attribute/:attribute',
      :namespaces => 'rest:///attribute',
      :namespace_config => 'rest:///attribute/:namespace/_meta',
      :config => 'rest:///attribute/:namespace/:attribute/_meta',
      :attributes => 'rest:///attribute/:namespace'

    map.connect :patchinfo, 'rest:///source/:project/:package/_patchinfo',
      :issues => 'rest:///source/:project/:package/?view=issues'
 
    # Statistics
    map.connect :latestadded, 'rest:///statistics/latest_added?:limit',
      :specific => 'rest:///statistics/added_timestamp/:project/:package'
    map.connect :downloadcounter, 'rest:///statistics/download_counter' +
      '?:project&:package&:arch&:repo&:group_by&:limit'
    map.connect :rating, 'rest:///statistics/rating/:project/:package',
      :all => 'rest:///statistics/highest_rated?:limit'
    map.connect :mostactiveprojects, 'rest:///statistics/most_active_projects?:limit',
      :specific => 'rest:///statistics/activity/:project'
    map.connect :mostactivepackages, 'rest:///statistics/most_active_packages?:limit',
      :specific => 'rest:///statistics/activity/:project/:package'

    map.connect :distribution, 'rest:///distributions/', all: 'rest:///distributions/include_remotes'

    map.connect :builddepinfo, 'rest:///build/:project/:repository/:arch/_builddepinfo?:package&:limit&:code'

  map.set_additional_header( 'User-Agent', "obs-webui/#{CONFIG['version']}" )
  map.set_additional_header( 'Accept', 'application/xml' )

  map.details = DetailsLogger.new

if defined?(Rack::MiniProfiler)
  ::Rack::MiniProfiler.profile_method(ActiveXML::Transport, :http_do) do |method,url| 
    if url.kind_of? String
      "#{method.to_s.upcase} #{url}"
    else
      "#{method.to_s.upcase} #{url.path}?#{url.query}" 
    end
  end
end

