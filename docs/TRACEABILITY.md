# Traceability Matrix – Library Book Management System

Purpose: Map requirements (user stories) to implementation and tests, and show when each was delivered.

| Req ID | User Story | Sprint | Implementation (Code) | Verification (Tests) | Release Tag | Status |
|--------|------------|--------|----------------------|--------------------|-------------|--------|
| US1 | Add a book | Sprint-1 | Library.add_book() | test_add_book_success, test_add_book_duplicate | v0.1  | Done |
| US2 | Borrow a book | Sprint-2 | Library.borrow_book() | test_borrow_book, test_borrow_unavailable_book | v0.2 | Done |
| US3 | Return a book | Sprint-2 | Library.return_book() | test_return_book | v0.2 | Done |
| US4 | Generate library report | Sprint-3 | Library.generate_report() | test_generate_report | v0.3 | Done |

