#!/usr/bin/env node

/**
 * automation-workflows - Local Workflow Automation Tool
 * No API required - 100% local operations
 */

const fs = require('fs');
const path = require('path');
const { execSync, exec } = require('child_process');

class AutomationWorkflows {
  constructor() {
    this.workspace = process.cwd();
  }

  // ==================== File Operations ====================

  async moveFiles(pattern, destination) {
    const files = this.findFiles(pattern);
    console.log(`Found ${files.length} files matching: ${pattern}`);
    
    for (const file of files) {
      const destPath = path.join(destination, path.basename(file));
      fs.renameSync(file, destPath);
      console.log(`✓ Moved: ${file} → ${destPath}`);
    }
    return files.length;
  }

  async copyFiles(pattern, destination) {
    const files = this.findFiles(pattern);
    console.log(`Found ${files.length} files matching: ${pattern}`);
    
    for (const file of files) {
      const destPath = path.join(destination, path.basename(file));
      fs.copyFileSync(file, destPath);
      console.log(`✓ Copied: ${file} → ${destPath}`);
    }
    return files.length;
  }

  async createFolderStructure(structure) {
    const parsed = JSON.parse(structure);
    this.createFolders(parsed, '.');
    console.log('✓ Folder structure created');
  }

  createFolders(structure, base) {
    for (const [name, content] of Object.entries(structure)) {
      const fullPath = path.join(base, name);
      if (typeof content === 'object') {
        fs.mkdirSync(fullPath, { recursive: true });
        this.createFolders(content, fullPath);
      } else {
        fs.writeFileSync(fullPath, content);
      }
    }
  }

  findFiles(pattern) {
    const glob = require('glob');
    return glob.sync(pattern);
  }

  // ==================== Git Operations ====================

  gitStatus() {
    try {
      const status = execSync('git status --porcelain', { encoding: 'utf8' });
      return status || 'Clean working tree';
    } catch {
      return 'Not a git repository';
    }
  }

  gitAutoCommit(message, push = false) {
    try {
      // Stage all changes
      execSync('git add .', { encoding: 'utf8' });
      
      // Sanitize commit message to prevent command injection
      const commitMsg = message || `Auto backup: ${new Date().toISOString()}`;
      const sanitizedMsg = commitMsg
        .replace(/"/g, '\\"')
        .replace(/;/g, '')
        .replace(/`/g, '')
        .replace(/\$/g, '');
      
      execSync(`git commit -m "${sanitizedMsg}"`, { encoding: 'utf8' });
      console.log('✓ Changes committed');
      
      // Push if requested
      if (push) {
        execSync('git push', { encoding: 'utf8' });
        console.log('✓ Changes pushed');
      }
      
      return true;
    } catch (error) {
      console.log('Nothing to commit or error:', error.message);
      return false;
    }
  }

  gitCreateBranch(branchName) {
    try {
      // Sanitize branch name to prevent command injection
      const sanitizedName = branchName
        .replace(/[^a-zA-Z0-9/_-]/g, '');
      execSync(`git checkout -b "${sanitizedName}"`, { encoding: 'utf8' });
      console.log(`✓ Created and switched to branch: ${sanitizedName}`);
      return true;
    } catch {
      console.log('Branch already exists or error');
      return false;
    }
  }

  // ==================== System Operations ====================

  async cleanupLogs(pattern = '*.log', maxAge = 7) {
    const files = this.findFiles(`**/${pattern}`);
    const now = Date.now();
    const maxAgeMs = maxAge * 24 * 60 * 60 * 1000;
    
    let deleted = 0;
    for (const file of files) {
      const stats = fs.statSync(file);
      if (now - stats.mtimeMs > maxAgeMs) {
        fs.unlinkSync(file);
        deleted++;
      }
    }
    
    console.log(`✓ Cleaned ${deleted} log files older than ${maxAge} days`);
    return deleted;
  }

  async runScheduledTask(taskName, schedule) {
    console.log(`Scheduled task "${taskName}" registered for: ${schedule}`);
    // In a full implementation, this would integrate with cron
    return { taskName, schedule, status: 'registered' };
  }

  // ==================== Export ====================

  getTools() {
    return {
      moveFiles: { pattern: 'string', destination: 'string' },
      copyFiles: { pattern: 'string', destination: 'string' },
      createFolderStructure: { structure: 'json' },
      gitStatus: {},
      gitAutoCommit: { message: 'string?', push: 'boolean?' },
      gitCreateBranch: { branchName: 'string' },
      cleanupLogs: { pattern: 'string?', maxAge: 'number?' }
    };
  }
}

// CLI Interface
if (require.main === module) {
  const args = process.argv.slice(2);
  const command = args[0];
  const workflow = new AutomationWorkflows();

  switch (command) {
    case 'move':
      workflow.moveFiles(args[1], args[2]);
      break;
    case 'copy':
      workflow.copyFiles(args[1], args[2]);
      break;
    case 'mkdir':
      workflow.createFolderStructure(args[1]);
      break;
    case 'status':
      console.log(workflow.gitStatus());
      break;
    case 'commit':
      workflow.gitAutoCommit(args[1], args[2] === '--push');
      break;
    case 'branch':
      workflow.gitCreateBranch(args[1]);
      break;
    case 'cleanup':
      workflow.cleanupLogs(args[1], parseInt(args[2] || 7));
      break;
    default:
      console.log('automation-workflows CLI');
      console.log('Commands: move, copy, mkdir, status, commit, branch, cleanup');
  }
}

module.exports = AutomationWorkflows;
