module GetFlags
  # FIXME: All of this would not be needed if creating an Package/Project would create all
  #        the build, publish, debuginfo and useforbuild Flags. The only reason
  #        this happens here is because rendering the XML does ignore the defaults.
  # Returns a hash of arrays, sorted by repository.
  # The arrays contain Flag objects of type, sorted by architecture.
  # Like:
  # {all: [Flag, Flag-i586, Flag-x86_64], 13.2: [Flag, Flag-i585, Flag-x86_64]}
  def get_flags(flag_type)
    the_flags = {}

    # [nil] is a placeholder for "all" repositories
    [nil].concat(repositories.pluck(:name)).each do |repository|
      the_flags[repository] = []
      # [nil] is a placeholder for "all" architectures
      [nil].concat(architectures.reorder('name').distinct).each do |architecture|
        architecture_id = architecture ? architecture.id : nil
        flagcount = 0
        pkgnames = flags.distinct.pluck(:pkgname)
        pkgnames.each do |pkgname|
          flag = flags
                   .where(flag: flag_type)
                   .where(repo: repository)
                   .where(architecture_id: architecture_id)
                   .where(pkgname: pkgname)
                   .first
          if flag
            the_flags[repository] << flag
            flagcount += 1
          end
        end
        # If there is no flag create a temporary one.
        if flagcount == 0
          flag = flags.new(flag: flag_type, repo: repository, architecture: architecture)
          flag.status = flag.effective_status
          the_flags[repository] << flag
        end
      end
    end
    the_flags['all'] = the_flags.delete(nil)

    the_flags
  end
end
