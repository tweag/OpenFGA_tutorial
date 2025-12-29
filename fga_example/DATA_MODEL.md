# Example Data Model and Access Control

This document explains the authorization model used in this OpenFGA tutorial and details who has access to what based on the configured relationships.

## Overview

The authorization model implements a document management system with hierarchical permissions. Users belong to editor teams, teams have access to folders, and documents inherit permissions from their parent folders.

## Entity Types

### Users

The system has 5 users:

| User ID           | Name            | Email                       |
| ----------------- | --------------- | --------------------------- |
| `anne_smith`      | Anne Smith      | anne.smith@example.com      |
| `bob_jones`       | Bob Jones       | bob.jones@example.com       |
| `clara_zhang`     | Clara Zhang     | clara.zhang@example.com     |
| `david_rodriguez` | David Rodriguez | david.rodriguez@example.com |
| `emily_patel`     | Emily Patel     | emily.patel@example.com     |

### Editor Teams

Two editor teams exist in the system:

- **team1**: Members can edit documents in folders assigned to this team
- **team2**: Members can edit documents in folders assigned to this team

### Folders

| Folder ID | Title               | Description                                             |
| --------- | ------------------- | ------------------------------------------------------- |
| `1`       | Cognitive Studies   | Research materials for cognitive psychology experiments |
| `2`       | Behavioral Analysis | Data collection for behavioral psychology research      |

### Documents

| Document ID | Title                        | Parent Folder | Published |
| ----------- | ---------------------------- | ------------- | --------- |
| `1`         | Behavioral Survey Results    | Folder 2      | No        |
| `2`         | Conditioning Experiment Data | Folder 2      | Yes       |
| `3`         | Behavioral Therapy Methods   | Folder 2      | No        |
| `4`         | Memory Formation Study       | Folder 1      | Yes       |
| `5`         | Attention Span Analysis      | Folder 1      | No        |
| `6`         | Cognitive Bias Research      | Folder 1      | Yes       |

## Authorization Model

The model defines the following relationships:

```
type user

type editors
  relations
    - member: [user]

type folder
  relations
    - editor: [editors#member]
    - reader: [user] or editor

type document
  relations
    - parent: [folder]
    - reader: reader from parent (inherited)
    - writer: editor from parent (inherited)
    - owner: [user] and editor from parent
```

### Key Concepts

- **Direct membership**: Users are explicitly members of editor teams
- **Inherited permissions**: Documents inherit reader and writer permissions from their parent folder
- **Conditional ownership**: A document owner must be explicitly assigned AND must also be an editor of the parent folder

## Configured Relationships

### Team Memberships

- **team1**:

  - Anne Smith (`anne_smith`)

- **team2**:
  - Bob Jones (`bob_jones`)
  - Clara Zhang (`clara_zhang`)

### Folder Access

- **Folder 1 (Cognitive Studies)**:

  - Editors: team2 members (Bob Jones, Clara Zhang)
  - Readers: Emily Patel

- **Folder 2 (Behavioral Analysis)**:
  - Editors: team1 members (Anne Smith)
  - Readers: David Rodriguez

### Document Ownership

- **Document 2** (Conditioning Experiment Data): Anne Smith
- **Document 6** (Cognitive Bias Research): Bob Jones

## Access Matrix

### Who Can Access What

| User                | Document 1  | Document 2             | Document 3  | Document 4  | Document 5  | Document 6             |
| ------------------- | ----------- | ---------------------- | ----------- | ----------- | ----------- | ---------------------- |
| **Anne Smith**      | Read, Write | Read, Write, **Owner** | Read, Write | -           | -           | -                      |
| **Bob Jones**       | -           | -                      | -           | Read, Write | Read, Write | Read, Write, **Owner** |
| **Clara Zhang**     | -           | -                      | -           | Read, Write | Read, Write | Read, Write            |
| **David Rodriguez** | Read        | Read                   | Read        | -           | -           | -                      |
| **Emily Patel**     | -           | -                      | -           | Read        | Read        | Read                   |

**Legend:**

- **Read**: Can view the document
- **Write**: Can edit the document
- **Owner**: Has ownership rights (must also be an editor of parent folder)
- **-**: No access

## Implementation Notes

The relationships are defined in `sample_tuples.json` and loaded into OpenFGA during setup. The model enforces:

1. **Hierarchical permissions**: Documents automatically inherit permissions from folders
2. **Role-based access**: Users gain access through team membership
3. **Separation of concerns**: Readers and editors have different capabilities
4. **Ownership constraints**: Owners must also be editors of the parent folder
